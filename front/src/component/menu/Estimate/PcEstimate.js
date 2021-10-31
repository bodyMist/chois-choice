import { Link } from "react-router-dom";
import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";
import PcRecommand from "./PcRecommand";
import axios from "axios";
import { useState } from "react";

export default function PcEstimate() {
    const [list, setList] = useState([]);
    const getPartInf=(id)=> {
        console.log(id);
        axios
        .get(`/api?${id}`)
        .then(({data})=>{
            setList({
                setList: data.Item
            })
        })
        .catch(e => {
            console.error(e);
        })
    }
    return (
        <div className="container">
            {/* <h3>PC 견적</h3> */}
            <Link to="/PcRecommand">견적 추천</Link>
            <div className="container-pc">
                <PartSelect list={list}/>
                <PartSelected getPartInf={getPartInf}/>
            </div>
        </div>
    );
}
