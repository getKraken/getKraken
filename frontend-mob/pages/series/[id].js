import React, { Component } from 'react'
import { getSeriesData } from '../../services/data-fetcher'
import { withRouter } from 'next/router'


// const SingleSeriesWithRouter = (props) => {
//     const router = useRouter()
//     return <SingleSeries {...props} router={router} />
//   }


class SingleSeries extends Component {

    constructor(props) {
        super(props);
        // console.log('query', props.router.query);

        this.state = {
            id: 9, //props.router.query.id,
            series: {
                title: '...',
                participants: []
            },
        }
    }

    async componentDidMount() {

        const { id } = this.props.router.query

        const series = await getSeriesData(id);

        this.setState({ series });

    }

    render() {
        return (
            <>
            <h1>Series {this.state.series.title}</h1>
            <ul>
                {this.state.series.participants.map(participant => (
                    <li>{participant.username}</li>
                ))}
            </ul>
            </>
        )
    }

}

export default withRouter(SingleSeries)

