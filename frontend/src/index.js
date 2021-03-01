import React, { Component } from "react";
import {render} from "react-dom";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      room: null
    }
  }

  componentDidMount() {
    fetch('api/get_room_messages/1/')
    .then(response => response.json())
    .then(data => console.log(data));

    console.log(this.props.room)
  }

  render() {
    return (
      <div> hello chat </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App {...(app.dataset)} />, container);