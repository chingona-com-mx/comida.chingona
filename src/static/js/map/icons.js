
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import { Icon, Style } from 'ol/style';
import { fromLonLat } from 'ol/proj';
import VectorSource from 'ol/source/Vector';
import { Vector as VectorLayer } from 'ol/layer';

const places = [
    {
        id: 1,
        location: [-99.14, 19.43],
        type: 'garnachas'
    },
    {
        id: 2,
        location: [-98.35, 17.84],
        type: 'antojitos'
    },
    {
        id: 3,
        location: [-98.93, 19.86],
        type: 'tacos'
    }
]

function createIcon(place) {
    const icon = new Feature({
        geometry: new Point(fromLonLat(place.location))
    })

    icon.setStyle(new Style({
        image: new Icon(({
            src: '/static/media/icons/icon_map.jpg',
            scale: 0.15
        }))
    }));

    return icon;
}
console.log(places.map(createIcon))
let vectorSource = new VectorSource({
    features: places.map(createIcon)
});

let vectorLayer = new VectorLayer({
    source: vectorSource
});

export default vectorLayer;
