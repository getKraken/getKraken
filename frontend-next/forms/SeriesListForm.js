import React from 'react';
import SubmitButton from '../components/SubmitButton';
import Router from 'next/router';
class SeriesListForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            disableButton: false
        }
    }
    routerseries(seriesId) {
        Router.push(`../pages/single-series/${seriesId}`)
    }
    render() {
        return (
            <>
                {this.props.seriesData.length ?
                    <ul>
                        {this.props.seriesData.map(series => (
                            <li key={series.id}>
                                <SubmitButton
                                    text={series.title}
                                    disabled={this.state.disableButton}
                                    onClick={() => this.routerseries(`${series.id}`)}
                                />
                            </li>
                        ))}
                    </ul>
                    : <h1>create something</h1>}
            </>
        )
    }
}
export default SeriesListForm;