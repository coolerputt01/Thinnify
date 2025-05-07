const { defineConfig } = require('@vue/cli-service')
const path = require('path')

module.exports = defineConfig({
  transpileDependencies: true,

  // ✅ Official PWA plugin config goes here — outside configureWebpack
  pwa: {
    name: 'Thinnify',
    themeColor: '#ff5d2b',
    manifestOptions: {
      short_name: 'Thinnify',
      icons: [
        {
          src: 'https://i.ibb.co/hxf6ZfkG/Thnnify-Thinnify-Thinnify-Logo.jpg',
          sizes: '192x192',
          type: 'image/jpg',
        },
        {
          src: 'https://i.ibb.co/hxf6ZfkG/Thnnify-Thinnify-Thinnify-Logo.jpg',
          sizes: '512x512',
          type: 'image/jpg',
        },
      ],
    },
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
      skipWaiting: true,
      clientsClaim: true,
    },
  },
})
