moment.tz.setDefault('Europe/Madrid'); // Set local hour

// Sumary table
var minSpeed = min(speeds.map(item => item.speed)).toFixed(2);
var maxSpeed = max(speeds.map(item => item.speed)).toFixed(2);
var avgSpeed = avg(speeds.map(item => item.speed)).toFixed(2);

document.getElementById('speed-min').innerHTML = minSpeed;
document.getElementById('speed-max').innerHTML = maxSpeed;
document.getElementById('speed-avg').innerHTML = avgSpeed;

// Rename JSON keys with t and y that are required by chartjs
speeds.forEach( obj => renameKey( obj, 'timestamp_utc_ms', 't'));
speeds.forEach( obj => renameKey( obj, 'speed', 'y'));

// Set min and max ticks
var minTick = min(speeds.map(item => item.t));
var maxTick = max(speeds.map(item => item.t));

var diff = maxTick - minTick;

if(diff > 3600 * 1000 * 13){
  maxTick = minTick + 3600 * 1000 * 13;
}

// Set stepSize in mins according to diff
var stepSize;

switch(true) {
  case (diff <= 15 * 60 * 1000): // 15 mins
    stepSize = 1;
    break;
  case (diff <= 20 * 60 * 1000): // 20 mins
    stepSize = 2;
    break;
  case (diff <= 30 * 60 * 1000): // 30 mins
    stepSize = 5;
    break;
  case (diff <= 60 * 60 * 1000): // 60 mins
    stepSize = 10;
    break;
  case (diff <= 120 * 60 * 1000):// 120 mins 
    stepSize = 15;
    break;
  case (diff <= 60 * 4 * 60 * 1000): // 4 hours
    stepSize = 30;
    break;
  default:
    stepSize = 60;
}

// Chart
new Chart('speed', {
  type: 'line',
  data: {
    datasets: [{
      label: 'Speed',      
      data: speeds,
      borderColor: '#FFCE56',
      backgroundColor: '#FFCE56',
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
          stepSize: 10,
          
        },
        scaleLabel: {
          display: true,
          labelString: 'km/h'
        }
      }],
      xAxes: [{
        type: 'time',
        time: {
          unit: 'minute',
          stepSize: stepSize,
          displayFormats: {
            minute: 'H:mm',
            hour: 'H:mm'
          },
          tooltipFormat: 'YYYY-MM-DD HH:mm:ss z'
        },
        ticks: {
          min: minTick,
          max: maxTick
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