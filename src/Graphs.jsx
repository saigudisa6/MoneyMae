import './graphs.css'
import Graph from './Graph';
function Graphs(){
    return(
        <div className="graphs-container">
            <Graph src={'../public/Screenshot 2023-11-05 at 3.28.01 AM.png'}/>
            <Graph src={'../public/Screenshot 2023-11-05 at 3.28.10 AM.png'}/>
        </div>
    )
}

export default Graphs;