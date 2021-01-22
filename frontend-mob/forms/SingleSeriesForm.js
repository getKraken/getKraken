import React from 'react';

class SingleSeriesForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      claimedEventsList: [],
      participantList: [],
      unclaimedEventsList: [],
      organizer: '',
      userID: 0,
      serieID: 0
      // i will use the self API to get to my username
    }
  }
  async componentDidMount(){
    let newClaimedEventsList = [];
    let newUnclaimedEventsList = [];
    router = useRouter();
    const {id} = router.query;
    const url = 'http://get-kraken.herokuapp.com/api/v1/event';
    let JWTToken = localStorage.getItem('kraken-access-token');
    let config = { headers: { "Authorization": `Bearer ${JWTToken}` } };
    const response = await axios.get(url, config)
    console.log(response.data)
  }


    // GET the API for the Events List
    // fetch('http://get-kraken.herokuapp.com/api/v1/event')
    //   .then(res => res.json())
    //   .then(result => {
    //     if (result.length != 0) {
    //       result.forEach(event => {
    //         // there might be a better way to do it but I do not know yet
    //         this.setState({
    //           serieID: event.series.id
    //         })
    //         if (event.host === this.state.userID) {
    //           newClaimedEventsList.push(event.description)
    //         }
    //         if (event.host === null) {
    //           newUnclaimedEvents.push(event.description)
    //         }
    //       })
    //     }
    //   })

    // this.setState({
    //   claimedEventsList: newClaimedEventsList,
    //   unclaimedEventsList: newUnclaimedEventsList
    // })


    // if (this.state.seriesID != 0) {
    //   //Get data from the series list of one series
    //   fetch(`http://get-kraken.herokuapp.com/api/v1/series/${this.state.serieID}`)
    //     .then(res => res.json())
    //     .then(result => this.setState({
    //       participantList: result.participants,
    //       organizer: result.organizer.username

    //     }))
    // }
  
  render() {
    return (
      <>
        {this.state.unclaimedEventsList.length ?
          <div className="unclaimedEventsList">
            <ul>
              {this.state.unclaimedEventsList.map(event => (
                <li>
                  {event}
                </li>
              ))}
            </ul>
          </div>
          : <h1> create an event </h1>}

        {this.state.claimedEventsList.length ?
          <div className="claimedEventsList">
            <ul>
              {this.state.claimedEventsList.map(event => (
                <li>
                  {event}
                </li>
              ))}
            </ul>
          </div>
          : ''}
        {this.state.participantList.length ?
          <div className="membersList">
            <ul>
              {this.state.participantList.map(participant => {
                if (participant.username === this.state.organizer) {
                  <li>
                    {participant.username} (Organizer)
                </li>
                } else {
                  <li>
                    {participant.username}
                  </li>
                }
              })}
            </ul>
          </div>
          : ''}
      </>
    )
  }
}

export default SingleSeriesForm





{/* <div className="unclaimedEventsList">
          <ul>
            {this.state.unclaimedEventsList.map(event => (
              <li>
                {event}
              </li>
            ))}
          </ul>
        </div>
        <div className="claimedEventsList">
          <ul>
            {this.state.claimedEventsList.map(event => (
              <li>
                {event}
              </li>
            ))}
          </ul>
        </div>
        <div className="membersList">
          <ul>
            {this.state.participantList.map(participant => {
              if (participant.username === this.state.organizer) {
                <li>
                  {participant.username} (Organizer)
                </li>
              } else {
                <li>
                  {participant.username}
                </li>
              }
            })}
          </ul>
        </div> */}