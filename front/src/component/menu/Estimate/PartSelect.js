import React, { useState } from "react";
import axios from "axios";
import PartList from "./PartList";

export default function PartSelect({list, selectPart}) {
    const handleClick = (e) => {
        axios
            .get("/api")
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    return (
        <div className="container-partSelect">
            <div className="parts">
                <div className="searchInputArea">
                    <div className="input-group">
                        <input
                            type="text"
                            className="form-control"
                            placeholder="부품 명 검색"
                        ></input>
                        <div className="input-group-btn">
                            <button
                                className="btn btn-default"
                                type="button"
                                onClick={handleClick}
                                id="search"
                            >
                                검색
                            </button>
                            <button className="btn btn-default" type="button">
                                초기화
                            </button>
                        </div>
                    </div>
                </div>
                <div className="scroll_box">
                    <table className="StuffListView">
                        <PartList list={list} selectPart={selectPart}/>
                    </table>
                </div>
            </div>
        </div>
    );
}
