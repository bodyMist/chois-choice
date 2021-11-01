import { Link } from "react-router-dom";
import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";
import axios from "axios";
import { useState } from "react";
import { useEffect } from "react";

export default function PcEstimate() {
  const [list, setList] = useState([]);
  const [sList, setSlist] = useState([
    { id: 1, name: "미선택" },
    { id: 2, name: "미선택" },
    { id: 3, name: "미선택" },
    { id: 4, name: "미선택" },
    { id: 5, name: "미선택" },
    { id: 6, name: "미선택" },
    { id: 7, name: "미선택" },
    { id: 8, name: "미선택" },
    { id: 9, name: "미선택" },
  ]);
  useEffect(() => {
    axios
      .get(`/api?id=1`)
      .then((response) => {
        setList(response.data);
      })
      .catch((e) => {
        console.error(e);
      });
  }, []);
  const getPartInf = (id) => {
    axios
      .get(`/api`, { params: { id } })
      .then((response) => {
        setList(response.data);
      })
      .catch((e) => {
        console.error(e);
      });
  };

  const selectPart = (component_id) => {
    const l = list.filter((list) => list.component_id == component_id)[0];
    let array = [...sList];
    array[l.data_type - 1] = { id: l.data_type, name: l.name };
    setSlist(array);
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
