const path = require('path');
const LiveReloadPlugin = require('webpack-livereload-plugin');

module.exports = {
    entry: './ebapp/index.js',
    output: {
        path: './static/js/',
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['','.js','.jsx','.scss']
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loaders: ['babel'],
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                loader: 'style!css!sass',
                exclude: /node_modules/
            }
        ]
    },
    plugins: [
        new LiveReloadPlugin()
    ]
};