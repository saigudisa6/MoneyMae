import './graphs.css'
import PropTypes from 'prop-types';

function Graph(props){
    const {src} = props;
    return (
        <div className="graph-container">
            <img src = {src} className="graph"/>
        </div>
    )
}

Graph.propTypes = {
    src: PropTypes.string.isRequired,
  };

export default Graph;