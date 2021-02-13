import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Drawer from '@material-ui/core/Drawer';
import FaceAppBody from './FaceAppBody';

class Title extends React.Component {
  render() {
    return (
      <h1>Face App</h1>
    );
  }
}

class FaceApp extends React.Component {
  render() {
    return (
      <div>
        <AppBar position="static">
          <Title></Title>
        </AppBar>
        <FaceAppBody></FaceAppBody>
      </div>
    );
  }
}

export default FaceApp;
