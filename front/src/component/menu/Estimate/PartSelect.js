import React, { useState, useEffect } from "react";
import PartList from "./PartList";
import Paging from "../../Paging";

export default function PartSelect({ list, selectPart, page, pageHandler, count }) {
// const [page, setPage] = useState(1);
// const [pList, setPList] = useState([]);
// useEffect(() => {
//   setPList([...list]);
// }, [])
// const pageHandler = (pg) => {
//   setPage(pg);
//   let array = [];
//   let start = (pg - 1) * 10;
//   for (let i = start; i < start + 10; i++) {
//     if(list[i])
//     array = [...array, list[i]];
//   }
//   setPList([...array]);
// };
// const setListByPage = (li) => {
//   let array = [];
//   let start = (page - 1) * 10;
//   for (let i = start; i < start + 10; i++) {
//       if(li[i])
//           array = [...array, li[i]];
//   }
//   setPList([...array]);
// };
  return (
    <div className="container-partSelect">
      <div className="parts">
        <div className="scroll_box">
          <table className="StuffListView">
            <PartList list={list} selectPart={selectPart} />
          </table>
        </div>
        <Paging page={page} count={count} pageHandler={pageHandler}/>
      </div>
      
    </div>
  );
}
