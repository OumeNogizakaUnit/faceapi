import React from 'react';
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
                <Title></Title>
                <FaceAppBody></FaceAppBody>
            </div>
        );
    }
}

export default FaceApp;
