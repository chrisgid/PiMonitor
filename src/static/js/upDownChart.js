(function () {
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
                        unit: 'day'
                    }
                }]
            },
            tooltips: {
                callbacks: {
                label: (item) => item.yLabel + ' Mb/s',
                },
            },
            elements: {
                line: {
                    tension: 0
                }
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
                        unit: 'day'
                    }
                }]
            },
            tooltips: {
                callbacks: {
                label: (item) => item.yLabel + ' Mb/s',
                },
            },
            elements: {
                line: {
                    tension: 0
                }
            }
        }
    });



    fetch('/api/results/recent/days/7').then(function(response) {
        return response.json();
    }).then(function(results) {
        var downValues = []
        var upValues =[]
        results.forEach(result => {
            var point = {
                t: new Date(result.timestamp),
                y: bytesToMegabits(result.value, 2)
            };
            if (result.type == 'up') {
                uploadDataset.data.push(point);
                upValues.push(result.value)
            }
            if (result.type == 'down') {
                downloadDataset.data.push(point)
                downValues.push(result.value)
            }
        });
        downChart.update();
        upChart.update();
        document.getElementById('downAvg').innerText = bytesToMegabits(average(downValues), 2) + 'Mb/s';
        document.getElementById('upAvg').innerText = bytesToMegabits(average(upValues), 2) + 'Mb/s';
    }).catch(function() {
            console.log("Error getting data from result API");
    });

    function bytesToMegabits(value, decimalPlaces) {
        return Math.round(((value / 125000) + Number.EPSILON) * (10 ** decimalPlaces)) / ( 10 ** decimalPlaces);
    }

    function average(arr) {
        return arr.reduce( ( p, c ) => p + c, 0 ) / arr.length;
    }
})()