import React, { Component } from "react";
import {render} from "react-dom";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
import Chat from './components/chat';
import Room from './components/room';

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/chat" component={Room} />
          <Route path="/chat/:room_name" component={Chat}/>
        </Switch>
      </Router>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App/>, container);