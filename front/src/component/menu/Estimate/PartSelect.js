import React, { useState, useEffect } from "react";
import PartList from "./PartList";
import Paging from "../../Paging";

export default function PartSelect({ list, selectPart, page, pageHandler, count }) {
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
