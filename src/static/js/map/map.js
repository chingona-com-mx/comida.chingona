import 'ol/ol.css';
import { Map, View } from 'ol';
import { Tile } from 'ol/layer';
import { OSM } from 'ol/source';
import { fromLonLat } from 'ol/proj';

import getVectorLayer from './icons';

const mapConfig = {
	target: 'map',
	layers: [
		new Tile({
			source: new OSM()
		}),
	],
	view: new View({
		center: fromLonLat([-99.14, 19.43]),
		zoom: 9
	})
}

/**
 * Agrega los iconos a la configuración inicial del mapa y lo crea
 */
getVectorLayer().then(vectorLayer => {
	mapConfig.layers.push(vectorLayer);
	const map = new Map(mapConfig);
});
