import { useState } from "react";
import PartsSelector from "./PartsSelector"
import PartsViewer from "./PartsViewer";
export default function Parts() {
  const [list, setList] = useState([]);
  const getPartItem = (id) => {
    console.log(id);
  }
  return (
    <div className="prodlist_wrap">
    <PartsSelector getPartItem={getPartItem} list={list} />
    <PartsViewer/>
    </div>
  );
}