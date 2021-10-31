import { Link } from "react-router-dom";
import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";
import axios from "axios";
import { useState } from "react";
import { useEffect } from "react";

export default function PcEstimate() {
    const [list, setList] = useState([]);
    const [sList, setSlist] = useState([]);
    useEffect(()=>{
        axios
            .get(`/api?type=1`)
            .then((response) => {
                setList(response.data);
            })
            .catch((e) => {
                console.error(e);
            });
    }, []);
    const getPartInf = (id) => {
        axios
            .get(`/api?type=${id}`)
            .then((response) => {
                setList(response.data);
            })
            .catch((e) => {
                console.error(e);
            });
    };

    const selectPart = (component_id) => {
        setSlist(list.filter((list) => list.component_id == component_id))
    };

    return (
        <div className="container">
            {/* <h3>PC 견적</h3> */}
            <Link to="/PcRecommand">견적 추천</Link>
            <div className="container-pc">
                <PartSelect list={list} selectPart={selectPart} />
                <PartSelected getPartInf={getPartInf} sList={sList} />
            </div>
        </div>
    );
}
