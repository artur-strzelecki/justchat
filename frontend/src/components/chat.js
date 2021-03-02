import React, { Component } from "react";
import {CircularProgress, Grid} from '@material-ui/core';

class Chat extends Component {
  constructor(props) {
    super(props);
    this.state = {
        messages: null,
        loaded: false,
        wrong: false,
    }
  }

  componentDidMount() {
    if (this.props.location.nickname === undefined)
    {
      window.location.pathname = '/chat';
    }

    if (this.props.location.room_id != undefined) 
    {
      const room_id = this.props.location.room_id;
      const url = 'http://127.0.0.1:8000/api/get_room_messages/' + room_id + '/';
      fetch(url)
      .then(response => response.json())
      .then(data => {
        this.setState({messages: data, loaded: true})
      })
      .catch(error => {
        this.setState({wrong: true})
      })
      
    } else
    {
      this.setState({wrong: true})
    }
  }

  render() {
    if (this.props.location.nickname === undefined)
    {
      return <h2> Something wrong </h2>
    }

    if (this.state.wrong) 
    {
      return <h2> Something wrong 2 </h2>
    }

    if (!this.state.loaded)
    {
      return (
        <Grid
          container
          direction="column"
          justify="center"
          alignItems="center"
          style={{width: '100%', height: '100%'}}>
              <CircularProgress size={80} />
        </Grid>
      );
    }

    return (
        <h2> chat </h2>
    );
  }
}

export default Chat;
