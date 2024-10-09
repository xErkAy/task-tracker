import moment from "moment";

function formatTime(time, includeTime = false) {
  return time
    ? includeTime
      ? moment(time).format("DD.MM.YYYY HH:mm:ss")
      : moment(time).format("DD.MM.YYYY")
    : "";
}

export { formatTime };
