/**
 * Adds Circles with bubbleInfo when tap over the Port of Valencia with a radius of 12 metres onto the map
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */

moment.tz.setDefault('Europe/Madrid'); // Set local hour

function addCircleToGroup(group, latitude, longitude, strokeColor, fillColor, html) {
  var circle = new H.map.Circle(
    // The central point of the circle
    {lat: latitude, lng: longitude},
    // The radius of the circle in meters
    12,
    {
      style: {
        strokeColor: strokeColor, // Color of the perimeter
        lineWidth: 2.5,
        fillColor: fillColor  // Color of the circle
      }
    }
  );

  // add custom data to the circle
  circle.setData(html);
  group.addObject(circle);
}

function addInfoBubble(map) {
  var group = new H.map.Group();

  map.addObject(group);

  // add 'tap' event listener, that opens info bubble, to the group
  group.addEventListener('tap', function (evt) {
    // event target is the marker itself, group is a parent event target
    // for all objects that it contains
    var bubble =  new H.ui.InfoBubble(evt.target.getCenter(), {
      // read custom data
      content: evt.target.getData()
    });
    // show info bubble
    ui.addBubble(bubble);
  }, false);

  var i;
  for (i = 0; i < mapData.length; i++) {
    var data = mapData[i];
    timestampUTC = data.timestamp_utc_ms
    latitude = data.latitude
    longitude = data.longitude
    speed = data.speed

    var strokeColor;
    var fillColor;

    if (speed < 22) {
      fillColor = 'rgba(255, 0, 0, 0.4)';
      strokeColor = 'rgba(178, 34, 34, 0.7)';
    } else if (speed < 39) {
      fillColor = 'rgba(255, 255, 0, 0.65)';
      strokeColor = 'rgba(204, 173, 0, 1)';
    } else {
      fillColor = 'rgba(80, 200, 120, 0.7)';
      strokeColor = 'rgba(9, 121, 105, 0.6)';
    }

    addCircleToGroup(group, latitude, longitude, strokeColor, fillColor, 
    '<div><b>' + moment.utc(timestampUTC).local().format('YYYY-MM-DD H:mm:ss') + '</b></div><div>'
    + moment().tz(moment.tz.guess()).format('z')
    + '</div><div>' + latitude + ', ' + longitude + '</div>'
    + '<div>' + speed + ' km/h</div>');
  }


}

/**
 * Boilerplate map initialization code starts below:
 */

//Step 1: initialize communication with the platform
// In your own code, replace variable window.apikey with your own apikey
var platform = new H.service.Platform({
  apikey: "7sjjFHmKMkR1tN3_UfjKHat8LVikOLeM-KRH0uSgNt8"
});
var defaultLayers = platform.createDefaultLayers();

/**
 * Step 2: initialize a map - this map is centered over the Port of Valencia
 * 
 *     - Entire Port:      center: {lat:39.44175050, lng:-0.31809820}, zoom: 13.45
 *     - North Port Zone:  center: {lat:39.45184322, lng:-0.31722914}, zoom: 14.45
 *     - South Port Zone:  center: {lat:39.42934826, lng:-0.33036307}, zoom: 14.45
 */
var map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map, {
  center: {lat:39.42858680, lng:-0.33136000},
  zoom: 14.45,
  pixelRatio: window.devicePixelRatio || 1
});
// add a resize listener to make sure that the map occupies the whole container
window.addEventListener('resize', () => map.getViewPort().resize());

//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

behavior.disable(H.mapevents.Behavior.WHEELZOOM);

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);

// Now use the map as required...

addInfoBubble(map);