# Import dependencies
from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
import pandas as pd
import os

# Flask Setup
app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/names')
def names():
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", convert_unicode=True, echo=False)
    
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Samples = Base.classes.samples
    
    sampleIDs = Samples.__table__.columns.keys()[1:]

    return (jsonify(sampleIDs))

@app.route('/otu')
def otu():
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", convert_unicode=True, echo=False)
    
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    OTUs = Base.classes.otu
    
    session = Session(bind=engine)

    OTU_results = (session
                   .query(OTUs.lowest_taxonomic_unit_found))
    
    OTU_description = [row[0] for row in OTU_results]
    
    return (jsonify(OTU_description))

@app.route('/metadata/<sample>')
def sampleInfo(sample='BB_000'):
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", convert_unicode=True, echo=False)
    
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    SampleMetadata = Base.classes.samples_metadata

    session = Session(bind=engine)

    sample = int(sample[3:])
    info_results = (session
                    .query(SampleMetadata.AGE,
                           SampleMetadata.BBTYPE,
                           SampleMetadata.ETHNICITY,
                           SampleMetadata.GENDER,
                           SampleMetadata.LOCATION,
                           SampleMetadata.SAMPLEID)
                    .filter(SampleMetadata.SAMPLEID == sample)
                    .group_by(SampleMetadata.SAMPLEID)
                    .all())

    AGE = [row[0] for row in info_results][0]
    BBTYPE = [row[1] for row in info_results][0]
    ETHNICITY = [row[2] for row in info_results][0]
    GENDER = [row[3] for row in info_results][0]
    LOCATION = [row[4] for row in info_results][0]
    SAMPLEID = [row[5] for row in info_results][0]

    BB_sample = {'AGE: ': AGE,
                 'BBTYPE: ': BBTYPE,
                 'ETHNICITY: ': ETHNICITY,
                 'GENDER: ': GENDER,
                 'LOCATION: ': LOCATION,
                 'SAMPLEID: ': SAMPLEID
                 }
    
    return jsonify(BB_sample)

@app.route('/wfreq/<sample>')
def sampleWfreq(sample='BB_000'):
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", convert_unicode=True, echo=False)
    
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    SampleMetadata = Base.classes.samples_metadata

    session = Session(bind=engine)

    sample = int(sample[3:])
    wfreq_results = (session
                     .query(SampleMetadata.WFREQ,
                            SampleMetadata.SAMPLEID)
                     .filter(SampleMetadata.SAMPLEID == sample)
                     .group_by(SampleMetadata.SAMPLEID)
                     .all())

    WFREQ = [row[0] for row in wfreq_results][0]
    SAMPLEID = [row[1] for row in wfreq_results][0]

    BB_sample_wfreq = {'WFREQ: ': WFREQ,
                       'SAMPLEID: ': SAMPLEID
                       }
    
    return jsonify(BB_sample_wfreq)

@app.route('/samples/<sample>')
def sampleIDValues(sample='BB_000'):
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite", convert_unicode=True, echo=False)
    
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Samples = Base.classes.samples
    
    session = Session(bind=engine)
  
    value_results = (session
                     .query(Samples)
                     .filter(getattr(Samples, sample) > 0)
                     .order_by(getattr(Samples, sample).desc())
                     .all())
    
    otu_ids = [row.otu_id for row in value_results]
    sample_values = [getattr(row, sample) for row in value_results]

    return jsonify([{'otu_ids': otu_ids, 'sample_values': sample_values}])

if __name__ == "__main__":
    app.run(debug=True)