import React from 'react';

class UnclaimedEventForm extends React.Component{
  constructor(props){
    supper(props);
    this.state={
      UnclaimedEventList:[]
    }
  }
  async doclaimed(){
    // when the event happen, this functio will post the event to become a claimed event
  }
  componentDidMount(){
    fetch(UnclaimedEventAPI)
      .then(res => res.json())
      // this result will give me all the event, so how can I disassociate ie from the claimed one??
        .then(result =>) 
    
  }
}





