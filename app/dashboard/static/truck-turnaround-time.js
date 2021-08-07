moment.tz.setDefault('Europe/Madrid'); // Set local hour

// Summary table
var minCurrentTTT = min(currentTTTs.map(item => item.y)).toFixed(2);
var maxCurrentTTT = max(currentTTTs.map(item => item.y)).toFixed(2);
var avgCurrentTTT = avg(currentTTTs.map(item => item.y)).toFixed(2);

var minImprovedTTT = min(improvedTTTs.map(item => item.y)).toFixed(2);
var maxImprovedTTT = max(improvedTTTs.map(item => item.y)).toFixed(2);
var avgImprovedTTT = avg(improvedTTTs.map(item => item.y)).toFixed(2);

document.getElementById('current-ttt-min').innerHTML = minCurrentTTT;
document.getElementById('current-ttt-max').innerHTML = maxCurrentTTT;
document.getElementById('current-ttt-avg').innerHTML = avgCurrentTTT;

document.getElementById('improved-ttt-min').innerHTML = minImprovedTTT;
document.getElementById('improved-ttt-max').innerHTML = maxImprovedTTT;
document.getElementById('improved-ttt-avg').innerHTML = avgImprovedTTT;

// Chart
new Chart('ttt', {
  type: 'line',
  data: {
    datasets: [{
      label: 'Current',      
      data: currentTTTs,
      borderColor: '#00BCD4',
      backgroundColor: '#00BCD4',
      lineTension: 0,
      pointRadius: 3,
      pointHitRadius: 14, 
      pointHoverRadius: 3,
      fill: 'false'
    },
    {
      label: 'Improved',      
      data: improvedTTTs,
      borderColor: '#E64A19',
      backgroundColor: '#E64A19',
      lineTension: 0,
      pointRadius: 3,
      pointHitRadius: 3, 
      pointHoverRadius: 3,
      fill: 'false',
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          stepSize: 20,
          max: 100
        },
        scaleLabel: {
          display: true,
          labelString: 'mins'
        }
      }],
      xAxes: [{
        type: 'time',
        time: {
          parser: 'H:mm',
          unit: 'hour',
          stepSize: 1,
          displayFormats: {
            hour: 'H:mm'
          },
          tooltipFormat: 'H:mm z'
        },
        ticks: {
          min: '06:00',
          max: '19:00'
        },
        gridLines: {
          display:false
        }
      }]      
    },
    legend: {
      display: false,
      align: 'end',
      labels: {
        fontSize: 10,
        boxWidth: 20,
        boxHeight: 10
      }
    }
  }
});


