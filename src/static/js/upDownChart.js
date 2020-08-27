var downloadLabel = 'Download Speed'
var downloadBackgroundColor = ['rgba(255, 99, 132, 0.2)'];
var downloadBorderColor = ['rgba(255, 99, 132, 1)'];

var uploadLabel = 'Upload Speed'
var uploadBackgroundColor = ['rgba(54, 162, 235, 0.2)'];
var uploadBorderColor = ['rgba(54, 162, 235, 1)'];

var lineBorderWidth = 1;

var uploadDataset = {
    label: uploadLabel,
    backgroundColor: uploadBackgroundColor,
    borderColor: uploadBorderColor,
    data: []
};

var downloadDataset = {
    label: downloadLabel,
    backgroundColor: downloadBackgroundColor,
    borderColor: downloadBorderColor,
    data: []
};


var ctx = document.getElementById('upDownChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: { datasets: [ downloadDataset, uploadDataset ]},
    options: {
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour'
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        tooltips: {
            callbacks: {
            label: (item) => item.yLabel + ' Mb/s',
            },
        }
    }
});

fetch('/api/result').then(function(response) {
    return response.json();
}).then(function(results) {
    results.forEach(result => {

        var point = {
            t: new Date(result.timestamp),
            y: Math.round(result.value / 125000)
        };
        if (result.type == 'up') {
            uploadDataset.data.push(point);
        }
        if (result.type == 'down') {
            downloadDataset.data.push(point)
        }
    });
    chart.update();
}).catch(function() {
        console.log("Error getting data from result API");
});



