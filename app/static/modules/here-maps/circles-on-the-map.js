/**
 * Adds a circle over New Delhi with a radius of 1000 metres onto the map
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */
 function addCircleToMap(map, latitude, longitude){
  map.addObject(new H.map.Circle(
    // The central point of the circle
    {lat: latitude, lng: longitude},
    // The radius of the circle in meters
    25,
    {
      style: {
        strokeColor: 'rgba(32, 83, 116, 0.6)', // Color of the perimeter
        lineWidth: 2,
        fillColor: 'rgba(0, 174, 188, 0.7)'  // Color of the circle
      }
    }
  ));
}

// Restrict map
function restrictMap(map){

  var bounds = new H.geo.Rect(39.45397759873276, -0.3098011130508769, 39.45266796331936, -0.30485714483822635);

  map.getViewModel().addEventListener('sync', function() {
    var center = map.getCenter();

    if (!bounds.containsPoint(center)) {
      if (center.lat > bounds.getTop()) {
        center.lat = bounds.getTop();
      } else if (center.lat < bounds.getBottom()) {
        center.lat = bounds.getBottom();
      }
      if (center.lng < bounds.getLeft()) {
        center.lng = bounds.getLeft();
      } else if (center.lng > bounds.getRight()) {
        center.lng = bounds.getRight();
      }
      map.setCenter(center);
    }
  });

  /*
  //Debug code to visualize where your restriction is
  map.addObject(new H.map.Rect(bounds, {
    style: {
        fillColor: 'rgba(55, 85, 170, 0.1)',
        strokeColor: 'rgba(55, 85, 170, 0.6)',
        lineWidth: 8
      }
    }
  ));
  */
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

//Step 2: initialize a map - this map is centered over New Delhi
var map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map, {
  center: {lat:39.451942, lng:-0.306823},
  zoom: 14.5,
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

addCircleToMap(map, 39.455756, -0.327362);
addCircleToMap(map, 39.457793, -0.325144);
addCircleToMap(map, 39.459466, -0.323379);
addCircleToMap(map, 39.460118, -0.321837);

addCircleToMap(map, 39.460157, -0.320627);
addCircleToMap(map, 39.459886, -0.319450);
addCircleToMap(map, 39.459265, -0.318407);
addCircleToMap(map, 39.458364, -0.317707);

addCircleToMap(map, 39.456022, -0.316081);
addCircleToMap(map, 39.455707, -0.315649);
addCircleToMap(map, 39.455306, -0.315498);
addCircleToMap(map, 39.453185, -0.314125);

addCircleToMap(map, 39.453185, -0.314125);
addCircleToMap(map, 39.452306, -0.313198);
addCircleToMap(map, 39.452186, -0.313120);
addCircleToMap(map, 39.452056, -0.313082);

addCircleToMap(map, 39.451837, -0.313171);
addCircleToMap(map, 39.451586, -0.313198);
addCircleToMap(map, 39.451356, -0.313107);
addCircleToMap(map, 39.450795, -0.311620);

addCircleToMap(map, 39.450801, -0.309985);
addCircleToMap(map, 39.450796, -0.309021);
addCircleToMap(map, 39.450730, -0.308426);
addCircleToMap(map, 39.450519, -0.308088);

addCircleToMap(map, 39.450515, -0.307675);
addCircleToMap(map, 39.450557, -0.307131);
addCircleToMap(map, 39.450438, -0.306768);
addCircleToMap(map, 39.450274, -0.306170);

addCircleToMap(map, 39.450076, -0.305573);
addCircleToMap(map, 39.449955, -0.305188);
addCircleToMap(map, 39.449802, -0.304711);
addCircleToMap(map, 39.449562, -0.303998);

addCircleToMap(map, 39.449380, -0.303462);
addCircleToMap(map, 39.449160, -0.303001);
addCircleToMap(map, 39.448965, -0.302765);
addCircleToMap(map, 39.448700, -0.302583);

addCircleToMap(map, 39.448476, -0.302508);
addCircleToMap(map, 39.448232, -0.302476);
addCircleToMap(map, 39.447843, -0.302487);
addCircleToMap(map, 39.447495, -0.302487);

restrictMap(map);