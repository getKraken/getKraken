import React from 'react';
import SubmitButton from '../components/SubmitButton'

class NewEventForm extends React.Component {
  render(){
    return (
      <div className="NewEventForm">
        <form>
            <input>Event Title</input>
            <input>Event Description</input>
            <input>Event Date</input>
            <SubmitButton>Add New Event to the Series</SubmitButton>
        </form>
      </div>
    );
  }

}

export default NewEventForm;