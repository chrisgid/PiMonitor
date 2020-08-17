var testData = {
    datasets: [
        {
            label: 'Download Speed',
            data: [{
                t: new Date('2020-08-14T08:00:00Z'),
                y: 22
            }, 
            {
                t: new Date(2020, 8, 13, 10),
                y: 33
            },
            {
                t: new Date(2020, 8, 13, 11),
                y: 43
            },
            {
                t: new Date(2020, 8, 13, 12),
                y: 56
            },
            {
                t: new Date(2020, 8, 13, 13),
                y: 68
            }],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        },
        {
            label: 'Upload Speed',
            data: [{
                t: new Date(2020, 8, 13, 9),
                y: 10
            }, 
            {
                t: new Date(2020, 8, 13, 10),
                y: 15
            },
            {
                t: new Date(2020, 8, 13, 11),
                y: 12
            },
            {
                t: new Date(2020, 8, 13, 12),
                y: 13
            },
            {
                t: new Date(2020, 8, 13, 13),
                y: 11.5
            }],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }
    ]
};

var ctx = document.getElementById('upDownChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: testData,
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
}).then(function(data) {
    
    // transform data for chart here
    
    console.log(data);
}).catch(function() {
    console.log("Error getting data from result API");
});
