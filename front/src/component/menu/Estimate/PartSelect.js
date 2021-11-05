import React, { useState } from "react";
import axios from "axios";
import PartList from "./PartList";

export default function PartSelect({ list, selectPart, searchPart, resetPart }) {
  const search = () => {
    const word = document.querySelector(".form-control").value;
    searchPart(word)
  };
  const reset = () => {
    resetPart()
  }

  const onKeyPress = (e) => {
    if(e.key==='Enter') {
      search()
    }
  }
  const none = {
    display: "none",
  }
  return (
    <div className="container-partSelect">
      <div className="parts">
        <div className="searchInputArea">
          <form className="input-group" onKeyPress={onKeyPress}>
            <input
              type="text"
              className="form-control"
              placeholder="부품 명 검색"
            ></input>
            <input type="text" style={none}/>
            <div className="input-group-btn">
              <button
                className="btn btn-default"
                type="button"
                onClick={search}
                id="search"
              >
                검색
              </button>
              <button className="btn btn-default" type="reset" onClick={reset} >
                초기화
              </button>
            </div>
          </form>
        </div>
        <div className="scroll_box">
          <table className="StuffListView">
            <PartList list={list} selectPart={selectPart} />
          </table>
        </div>
      </div>
    </div>
  );
}
