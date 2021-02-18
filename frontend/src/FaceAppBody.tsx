import React from 'react';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';
import axios from './axiosconfig';

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
  image_data: Blob;
  result_str: string;
}

class FaceInputForm extends React.Component<{}, IState> {
  constructor(props: any) {
    super(props);
    this.state = {
      image_src: "",
      image_data: new Blob(),
      result_str: ""
    }
    this.handleChangeFile = this.handleChangeFile.bind(this);
    this.handleSubmitFile = this.handleSubmitFile.bind(this);
  }

  handleSubmitFile(event: React.FormEvent<HTMLInputElement>) {
    console.log("送信開始")
    const fd = new FormData();
    fd.append("file", this.state.image_data);
    fd.append("modelid", "0");
    const request_url: string = "http://localhost:8000/api/v1/locations";
    axios.post(request_url, fd, {
    }).then((responce) => {
      console.log(responce)
      const result_json = JSON.stringify(responce.data);
      this.setState({
        result_str: result_json
      })
    }).catch((e) => {
      console.log(e);
      this.setState({
        result_str: "通信に失敗しました"
      });
    });
  }

  handleChangeFile(event: React.ChangeEvent<HTMLInputElement>) {
    if(event.target instanceof HTMLInputElement && event.target.files) {
      const file = event.target.files[0];
      const image_url = URL.createObjectURL(file);
      this.setState({
        image_src: image_url,
        image_data: file
      });
    }
  }

  result(): JSX.Element {
    return (
      <pre>{this.state.result_str}</pre>
    )
  }

  preview(): JSX.Element {
    return (
      <img
        src={this.state.image_src}
        alt="画像プレビュー"
      ></img>
    )
  }

  inputfileform(): JSX.Element {
    const inputstyle: React.CSSProperties = {
      display: 'none'
    };
    return (
      <form>
        <input
          id="upload-file"
          type="file"
          accept="image/*"
          onChange={this.handleChangeFile}
          style={inputstyle}
        ></input>
        <label
          htmlFor="upload-file"
        >
          <Button
            variant="contained"
            color="primary"
            component="span">
            画像選択
          </Button>
        </label>
        <input
          id="submit"
          type="button"
          value="画像識別開始"
          onClick={this.handleSubmitFile}
          style={inputstyle}
        ></input>
        <label
          htmlFor="submit"
        >
          <Button
            variant="contained"
            color="secondary"
            component="span">
            画像アップロード
          </Button>
        </label>
      </form>
    )
  }

  render(){
    return (
      <div>
        {this.inputfileform()}
        {this.preview()}
        {this.result()}
      </div>
    );
  }
}

export default FaceAppBody;
