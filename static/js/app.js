// Dropdown menu of sample names
var namesURL = '/names';

Plotly.d3.json(namesURL, function(error, selectSamples) {
    if (error) {
        return console.warn(error);
    };

    selectSamples.forEach(function(name) {
        Plotly.d3
            .select("#selDataset")
            .append('option')
            .attr('value', name)
            .attr('class', 'dropdown')
            .text(name)
    });

});

// Function that changes event when a new sample is selected 
// (i.e. fetch data for the newly selected sample)
function optionChanged(sampleName) {

    // Endpoints for each sample
    var sampleRoute = '/sample/${sampleName}';
    var otuRoute = '/otu';
    var sampleMetadataRoute = '/metadata/${sampleName}';
    var wfreqRoute = 'wfreq/${sampleName}';

    // Endpoint for '/sample/${sampleName}'
    Plotly.d3.json(sampleRoute, function(error, selectSampleName) {
        if (error) {
            return console.warn(error);
        };

        // Variables to display on pie chart
        var sampleValues = selectSampleName.sample_values;
        var sampleIDs = selectSampleName.otu_ids;
        
        // Show only 10 sample_values and otu_ids on pie chart
        var chartValues = sampleValues.slice(0, 10);
        var chartLabels = sampleIDs.slice(0, 10);

        // Endpoint for '/otu'
        Plotly.d3.json(otuRoute, function(error, selectOtu) {
            if (error) {
                return console.warn(error);
            }
        
            // Variable to display otu description as hover text on pie chart
            // Create list to store all descriptions
            var otuDescriptions = []
            chartLabels.forEach(function(description) {
                otuDescriptions.push(selectOtu[description]);
            })

            // Show only 10 otuDescriptions for hover text
            var chartDescriptions = otuDescriptions.slice(0, 10);

            // Endpoint for '/metadata/${sampleName}'
            Plotly.d3.json(sampleMetadataRoute, function(error, selectMetadata) {
                if (error) {
                    return console.warn(error);
                }

                // Variables to display sample metadata info in box under dropdown
                var age = selectMetadata.AGE;
                var bbtype = selectMetadata.BBTYPE;
                var ethnicity = selectMetadata.ETHNICITY;
                var gender = selectMetadata.GENDER;
                var location = selectMetadata.LOCATION;
                var sampleID = selectMetadata.SAMPLEID;

                // Endpoint for 'wfreq/${sampleName}'
                Plotly.d3.json(wfreqRoute, function(error, selectWfreq) {
                    if (error) {
                        return console.warn(error);
                    }

                    

                })

            })
        })
    })
}