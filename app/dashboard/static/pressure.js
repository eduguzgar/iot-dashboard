moment.tz.setDefault('Europe/Madrid'); // Set local hour

var pressures = [
  { "t": '2018-08-15T10:06:01.339Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T10:16:13.914Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T10:22:03.147Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T10:32:14.335Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T10:40:01.339Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T10:56:13.914Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:02:03.147Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:05:14.335Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:07:01.339Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:10:13.914Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:22:03.147Z', y: randomNumber(1.0182, 1.0225, 4) },
  { "t": '2018-08-15T11:46:14.335Z', y: randomNumber(1.0182, 1.0225, 4) },
];

// Summary table
var minPressure = min(pressures.map(item => item.y)).toFixed(3);
var maxPressure = max(pressures.map(item => item.y)).toFixed(3);
var avgPressure = avg(pressures.map(item => item.y)).toFixed(3);

document.getElementById('pressure-min').innerHTML = minPressure;
document.getElementById('pressure-max').innerHTML = maxPressure;
document.getElementById('pressure-avg').innerHTML = avgPressure;

// Chart
new Chart('pressure', {
  type: 'line',
  data: {
    datasets: [{
      label: 'Pressure',      
      data: pressures,
      borderColor: '#cc65fe',
      backgroundColor: '#cc65fe',
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
          stepSize: 0.001
        },
        scaleLabel: {
          display: true,
          labelString: 'hPa'
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
              fontSize: 11
            }
    }
  }
});