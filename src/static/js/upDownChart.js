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


var downCtx = document.getElementById('downChart').getContext('2d');
var downChart = new Chart(downCtx, {
    type: 'line',
    data: { datasets: [ downloadDataset ]},
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

var upCtx = document.getElementById('upChart').getContext('2d');
var upChart = new Chart(upCtx, {
    type: 'line',
    data: { datasets: [ uploadDataset ]},
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



fetch('/api/results').then(function(response) {
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
    downChart.update();
    upChart.update();
}).catch(function() {
        console.log("Error getting data from result API");
});



