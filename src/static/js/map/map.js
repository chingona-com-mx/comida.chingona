import 'ol/ol.css';
import { Map, View } from 'ol';
import { Tile } from 'ol/layer';
import { OSM } from 'ol/source';
import { fromLonLat } from 'ol/proj';

import vectorLayer from './icons'


let map = new Map({
	target: 'map',
	layers: [
		new Tile({
			source: new OSM()
		}),
		vectorLayer
	],
	view: new View({
		center: fromLonLat([-99.14, 19.43]),
		zoom: 9
	})
});