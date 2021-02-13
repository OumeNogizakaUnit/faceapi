import React from 'react';

class FaceAppBody extends React.Component {
    render() {
        return (
            <div className="FaceAppBody">
                <p>顔画像を読み込むお</p>
                <FaceInputForm></FaceInputForm>
            </div>
        );
    }
}

interface IState {
    image_src: string;
}

class FaceInputForm extends React.Component<{}, IState> {
    constructor(props: any) {
        super(props);
        this.state = {
            image_src: "" 
        }
        this.handleChangeFile = this.handleChangeFile.bind(this);
    }

    handleChangeFile(event: React.FormEvent<HTMLFormElement>) {
        if(event.target instanceof HTMLInputElement && event.target.files) {
            const file = event.target.files[0];
            const image_url = URL.createObjectURL(file);
            this.setState({image_src: image_url});
        }
    }

    preview(): JSX.Element {
        return (
            <img
                src={this.state.image_src}
            ></img>
        )
    }

    render(){
        return (
            <div>
                <form
                    method="POST"
                    encType="multipart/form-data"
                    onChange={this.handleChangeFile}
                >
                    <input
                        id="upload-file"
                        type="file"
                        accept="image/*"
                    >
                    </input>
                    <label
                        htmlFor="upload-file"
                    >
                        アップロードする画像
                    </label>
                </form>
                <p>
                    {this.preview()}
                </p>
            </div>
        );
    }
}

export default FaceAppBody;
