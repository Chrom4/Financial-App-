const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');
const path = require('path');

const monorepoRoot = path.resolve(__dirname, '../..');

const config = {

  watchFolders: [monorepoRoot],

  resolver: {
    unstable_enableSymlinks: true,

    nodeModulesPaths: [path.resolve(monorepoRoot, 'node_modules')],
  },
};

module.exports = mergeConfig(getDefaultConfig(__dirname), config);