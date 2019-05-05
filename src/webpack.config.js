const path = require('path');

module.exports = {
  entry: './static/js/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'static/dist')
  },
  mode: 'development'
};