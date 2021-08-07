moment.tz.setDefault('Europe/Madrid'); // Set local hour

var humiditys = [
  { t: '2018-08-15T10:06:01.339Z', y: randomInt(56, 64) },
  { t: '2018-08-15T10:16:13.914Z', y: randomInt(56, 64) },
  { t: '2018-08-15T10:22:03.147Z', y: randomInt(56, 64) },
  { t: '2018-08-15T10:32:14.335Z', y: randomInt(56, 64) },
  { t: '2018-08-15T10:40:01.339Z', y: randomInt(56, 64) },
  { t: '2018-08-15T10:56:13.914Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:02:03.147Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:05:14.335Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:07:01.339Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:10:13.914Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:22:03.147Z', y: randomInt(56, 64) },
  { t: '2018-08-15T11:46:14.335Z', y: randomInt(56, 64) },
];

// Sumary table
var minHumidity = Math.round(min(humiditys.map(item => item.y)));
var maxHumidity = Math.round(max(humiditys.map(item => item.y)));
var avgHumidity = Math.round(avg(humiditys.map(item => item.y)));

document.getElementById('humidity-min').innerHTML = minHumidity;
document.getElementById('humidity-max').innerHTML = maxHumidity;
document.getElementById('humidity-avg').innerHTML = avgHumidity;

// Chart
new Chart('humidity', {
  type: 'line',
  data: {
    datasets: [{
      label: 'Humidity',      
      data: humiditys,
      borderColor: '#9CCC65',
      backgroundColor: '#9CCC65',
      lineTension: 0,
      pointRadius: 3,
      pointHitRadius: 14, 
      pointHoverRadius: 3,
      fill: 'false'
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
          min: 0,
          max: 100
        },
        scaleLabel: {
          display: true,
          labelString: '%'
        }
      }],
      xAxes: [{
        type: 'time',
        time: {
          unit: 'hour',
          stepSize: 0.25,
          displayFormats: {
            hour: 'H:mm'
          },
          tooltipFormat: 'YYYY-MM-DD HH:mm:ss z'
        },
        ticks: {
          
          min: '6:00', 
          max: '13:00' 
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
              fontSize: 10
            }
    }
  }
});