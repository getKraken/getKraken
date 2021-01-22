import React, { Component } from 'react'
import { getSeriesData, getEventData } from '../../services/data-fetcher'
import { withRouter } from 'next/router'


class SingleSeries extends Component {

    constructor(props) {
        super(props);
        // console.log('query', props.router.query);

        this.state = {
            id: 9, //props.router.query.id,
            series: {
                title: '...',
                participants: [],
            },
            events: [],
        }
    }

    async componentDidMount() {

        // const { id } = 9; //this.props.router.query;

        const id = 9;

        // console.log('id',id);

        const series = await getSeriesData(id);

        console.log('series', series);

        const allEvents = await getEventData();

        // console.log('allEvents', allEvents);

        const events = allEvents.filter(event => {
            return event.series.id === id;
        });

        console.log('events', events);

        this.setState({ series, events });



    }

    getDraftOrder() {
        const usernames = {}
        const people = this.state.series.participants;
        people.forEach( person => usernames[person.id] = person.username );
        
        const draft_data = JSON.parse(this.state.series.draft_order).draft_order;

        let output = draft_data.map( round => {
            return round.map( id => usernames[id] );
        })

        for(let i = 0; i<output.length; i++)
            output[i] = output[i].join(", ")

        return output
    }

    render() {
        return (
            <>
                <section className="text-gray-700 body-font">
                    <div className="container px-8 mx-auto pt-36 lg:px-4">
                        <div className="w-3/4 text-center mx-auto">

                            <h1 className="text-4xl mb-8">Series: {this.state.series.title}</h1>

                            <section className="my-6">
                                <h2 className="text-2xl mb-4">Participants</h2>
                                <ul>
                                    {this.state.series.participants.map(participant => (
                                        <li className="text-sm" key={participant.id}>{participant.username}</li>
                                    ))}
                                </ul>
                            </section>

                            <section className="my-6">

                                <h2 className="text-2xl mb-4">Draft Information</h2>

                                {this.state.series.round ? (

                                    <div>
                                        <h3>Draft Order</h3>
                                        {this.getDraftOrder().map( (round,i) => (
                                            <div key={i}>Round {i+1}: {round}</div>
                                        ))}
                                        <h3>Current Round: {this.state.series.round}</h3>
                                        <h3>Current Pick: {this.state.series.pick}</h3>
                                    </div>

                                ) : (
                                        <div className="my-4">
                                            <h3 className="my-4 text-sm italic">{this.state.series.draft_order}</h3>
                                            <button className="bg-blue-400 px-4 py-2 rounded hover:bg-blue-200">Generate Draft</button>
                                        </div>

                                    )}
                            </section>

                            <section className="my-6">
                                <h2 className="text-2xl mb-4">Events</h2>
                                <ul>
                                    {this.state.events.map(event => (
                                        <li className="text-sm" key={event.id}>{event.description}</li>
                                    ))}
                                </ul>
                            </section>

                            <button className="bg-blue-400 px-4 py-2 rounded hover:bg-blue-200">Create Event</button>
                        </div>
                    </div>
                </section>
            </>
        )
    }

}

export default withRouter(SingleSeries)

/*     <h2>Events</h2>
            <ul>
                {this.state.series.events.map(event => (
                    <li key={event.id}>{event.description}</li>
                ))}
            </ul>  */
