var webpack = require('webpack');
var path = require('path');

var plugins = [
  new webpack.DefinePlugin({
    'process.env.NODE_ENV':
      JSON.stringify(process.env.NODE_ENV || 'development')
  })
]

if (process.env.NODE_ENV === 'production') {
  plugins.push(new webpack.optimize.UglifyJsPlugin({
      compress: { warnings: false }
    })
  )
}

module.exports = {
  context: __dirname,
  entry: [
    path.resolve(__dirname, 'frontend', 'entry.js')
  ],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static')
  },
  plugins: plugins,
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        query: {
          presets: ["react", "latest"]
        }
      }
    ]
  },
  devtool: 'source-map',
  resolve: {
    extensions: ['.js', '.jsx']
  },
};
