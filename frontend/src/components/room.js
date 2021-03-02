import React, { Component } from "react";
import {render} from "react-dom";
import { makeStyles, withStyles } from '@material-ui/core/styles';
import {CircularProgress, Grid, TextField, Card, CardActionArea, CardContent, Typography } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom'
import Link from '@material-ui/core/Link'

class Room extends Component {
  constructor(props) {
    super(props);
    this.state={
      rooms: null,
      loaded: false,
      nickname: null,
    }
  }

  componentDidMount() {
    const url = 'http://127.0.0.1:8000/api/get_rooms/'
    fetch(url)
    .then(response => response.json())
    .then(data => {
      this.setState({rooms: data, loaded: true});
    });
  }

  handleLink(event) {
    if (this.state.nickname === null)
    {
      event.preventDefault()
    }
  }

  render() {
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
        <Grid
          container
          direction="column"
          justify="center"
          alignItems="center"
          style={{width: '100%', height: '100%', background: 'linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(52,108,191,1) 44%, rgba(0,212,255,1) 100%)'}}
        >
          <h1> JustChat </h1>
            <TextField style={{marginBottom: 20}} autoFocus={true} required={true} id="outlined-search" label="Nickname" type="search" variant="outlined" 
                       onChange={event => {
                        const { value } = event.target;
                        this.setState({ nickname: value });
                       }} />
          <Grid
            container
            direction="row"
            justify="center"
            alignItems="center"
            style={{width: '50%'}}
          >
          {this.state.rooms.map(item => {
            return (
              <Link onClick={this.handleLink.bind(this)} underline='none' component={RouterLink} to={{pathname: '/chat/' + item.name , nickname: this.state.nickname, room_id: item.id }} >
                  <Card style={{maxWidth: 200, borderRadius: 25, margin: 10}}>
                  <CardActionArea style={{width: '150', height: '100', background: '#00d4ff', textAlign: 'center'}}>
                    <CardContent>
                      <Typography gutterBottom variant="overline" style={{fontSize: 17,}}>
                        {item.name}
                      </Typography>
                      <Typography variant="body2" color="textSecondary" component="p">
                        Online: {item.id}
                      </Typography>
                    </CardContent>
                  </CardActionArea>
                </Card>
              </Link> 
            )
          })}
          </Grid>
      </Grid>
    );
  }
}

export default Room;
