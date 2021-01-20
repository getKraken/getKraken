import React from 'react';
import SubmitButton from '../components/SubmitButton'

class NewSeriesForm extends React.Component {
  render(){
    return (
      <div className="newSeriesForm">
        <form>
            <input>Series Title</input>
            <input>Series Description</input>
            <SubmitButton>Create New Series</SubmitButton>
        </form>
      </div>
    );
  }

}

export default NewSeriesForm;