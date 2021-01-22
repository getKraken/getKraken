import React from 'react';
import SubmitButton from '../components/SubmitButton'

class NewEventForm extends React.Component {
  render(){
    return (
      <div className="NewEventForm">
        <form>
            <label for='event-title'>Event Title:</label>
            <input type='text' id='event-title'>Event Title</input>

            <label for='event-description'>Event Description:</label>
            <input type='text' id='event-date'>Event Description</input>

            <label for='event-date'>Event Date:</label>
            <input type='text' id='event-date'>Event Date</input>
            
            <SubmitButton>Add New Event to the Series</SubmitButton>
        </form>
      </div>
    );
  }

}

export default NewEventForm;