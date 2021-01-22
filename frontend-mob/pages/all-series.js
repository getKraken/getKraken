import NavBar from '../components/NavBar';
import SeriesListForm from '../forms/SeriesListForm';
import React from 'react';
import { getSeriesData } from '../services/data-fetcher'

export default class AllSeries extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            seriesData: []
        }
    }

    async componentDidMount() {

        const seriesData = await getSeriesData();

        this.setState({ seriesData });
    }

    render() {
        return (
            <div className="SeriesListPage">
                <NavBar />
                <SeriesListForm seriesData={this.state.seriesData} />
            </div>
        )
    }
}




