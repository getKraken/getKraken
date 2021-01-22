import NavBar from '../components/NavBar'
import NewSeriesForm from '../forms/NewSeriesForm'
import NewEventForm from '../forms/NewEventForm'
import InviteUserForm from '../forms/InviteUserForm'

// TODO: Assign the currently signed in user that is creating the series to be the organizer of the series
export default function NewSeries(){
  return(

    <div className="NewSeriesPage">
      <NavBar/>

      <label for='full-new-series-form'>New Series Form</label>
      <div id='full-new-series-form'>
        
        <NewSeriesForm/>

        <label for='new-event-form'>Add an Event to your Series</label>
        <div id='new-event-form'>
          <NewEventForm/>  
        </div>

        <label for='invite-user-form'>Invite a friend</label>
        <div id='invite-user-form'>
          <InviteUserForm/>
        </div>

      </div>
    </div>  
  )
}