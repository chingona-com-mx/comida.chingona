
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import { Icon, Style } from 'ol/style';
import { fromLonLat } from 'ol/proj';
import VectorSource from 'ol/source/Vector';
import { Vector as VectorLayer } from 'ol/layer';

/**
 * Crear un punto
 */
function createIcon(place) {
    const icon = new Feature({
        geometry: new Point(fromLonLat(place.geometry.coordinates))
    })

    icon.setStyle(new Style({
        image: new Icon(({
            src: '/static/media/icons/icon_map.jpg',
            scale: 0.15
        }))
    }));

    return icon;
}

/**
 * Crea el Layer que contiene a todos los lugares de comida
 * guardados en la base de datos
 */
async function getVectorLayer() {

    let places = await fetch('/lugares/')
                .then(resp => resp.json())
                .then(data => data.features )

    let vectorSource = new VectorSource({
        features: places.map(createIcon)
    });

    let vectorLayer = new VectorLayer({
        source: vectorSource
    });

    return vectorLayer;
}

export default getVectorLayer;
