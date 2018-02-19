// Dropdown menu of sample names

var namesURL = '/names';

Plotly.d3.json(namesURL, function(error, selectSamples) {
    if (error) {
        return console.warn(error)
    };

    selectSamples.forEach(function(name) {
        Plotly.d3
            .select("selDataSet")
            .append('option')
            .attr('value', name)
            .attr('class', 'dropdown')
            .text(name)
    });

});
//     })
// }

// dropdown();







// function init() {
//     var data = [{
//         values: [
//             19, 26, 55, 88
//         ],
//         labels: [
//             "Spotify", "Soundcloud", "Pandora", "Itunes"
//         ],
//         type: "pie"
//     }];

//     var layout = {
//         height: 600,
//         width: 800
//     };

//     Plotly.plot("pie", data, layout);
// }

// function updatePlotly(newdata) {
//     // Update the pie chart with the newdata array
//     var $pie = document.getElementById("pie");
//     Plotly.restyle($pie, "values", [newdata]);
// }

// // This function will get called from the dropdown event handler.
// function getData() {
//     var data = [];
//     // Retrieve the value of the dropdown menu
//     var dataset = document.getElementById('selDataset').value;

//     // Select data array (YOUR CHOICE) depending on the value
//     // of the dropdown menu.

//     switch (dataset) {
//     case "dataset1":
//         data = [
//             19, 26, 55, 88
//         ];
//         break;
//     case "dataset2":
//         data = [
//             10, 20, 30, 37
//         ];
//         break;
//     case "dataset3":
//         data = [
//             100, 200, 300, 23
//         ];
//         break;
//     default:
//         data = [
//             1, 1, 1, 1
//         ];
//     }

//     // Update plot with new data
//     updatePlotly(data);
// }

// init();
