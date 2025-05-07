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
          src: 'https://i.ibb.co/DDRmhmFj/Thnnify-Thinnify-Thinnify-Logo.png',
          sizes: '192x192',
          type: 'image/png',
        },
        {
          src: 'https://i.ibb.co/DDRmhmFj/Thnnify-Thinnify-Thinnify-Logo.png',
          sizes: '512x512',
          type: 'image/png',
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
