import React, { Component } from "react";
import {render} from "react-dom";

class Chat extends Component {
  constructor(props) {
    super(props);
    this.state = {
        messages: null,
    }
  }

  /*componentDidMount() {
    const room_id = this.props;
    const url = 'api/get_room_messages/' + room_id + '/';
    fetch(url)
    .then(response => response.json())
    .then(data => console.log(data));
  }*/

  render() {
    return (
        <h2> chat </h2>
    );
  }
}

export default Chat;
