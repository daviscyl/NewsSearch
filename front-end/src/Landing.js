import { Input, AutoComplete } from "antd";
import React, { Component } from "react";
import "./Landing.css";
import NewsList from "./NewsList";
import Companise from "./Companies";

const { Search } = Input;

const newsapi = "https://newsapi.org/v2/everything?q=stock%20market&sort=popularity&from=";
const news_apikey = "&apiKey=1e4f8ec94dd04a618818e279de286283";

class Landing extends Component {
  constructor(props) {
    super(props);
    this.state = {
      listData: [],
      showHeadline: true,
    };
  }

  componentDidMount() {
    const today = new Date();
    let yesterday = new Date(today);
    yesterday.setDate(yesterday.getDate() - 3);
    const from =
      yesterday.getFullYear() +
      "-" +
      ("0" + (yesterday.getMonth() + 1)).slice(-2) +
      "-" +
      ("0" + yesterday.getDate()).slice(-2);
    const url = newsapi + from + news_apikey;

    fetch(url)
      .then((res) => res.json())
      .then((json) => {
        this.setState({ listData: json.articles });
      });
  }

  handleSearch = (query) => {
    fetch("http://ec2-54-215-128-254.us-west-1.compute.amazonaws.com:5000/" + query)
      .then((res) => res.json())
      .then((json) => {
        let list = [];
        json.forEach((e) => {
          list.push(e["_source"]);
        });
        return list;
      })
      .then((list) => {
        this.setState({ listData: list });
      });
  };

  render() {
    return (
      <div className="landing-page">
        <h1>NEU CS6200 Final Project Demo</h1>
        <h2>S&P-500 Company News Search - Davis (Yik Lung) Chan</h2>
        <div id="search-bar">
          <AutoComplete
            options={Companise}
            filterOption={(inputValue, option) => option.value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1}
          >
            <Search
              placeholder="Search S&P 500 Companise"
              size="large"
              onSearch={(query) => {
                this.handleSearch(query);
              }}
              enterButton
            />
          </AutoComplete>
        </div>
        <div className="head-lines">
          <NewsList listData={this.state.listData} />
        </div>
      </div>
    );
  }
}

export default Landing;
